const mediaobjects = nl_vpro_domain_media_MediaObjects;
const POMS_LOOKUP_URL = 'https://pomslookup.eo.nl';
const POPUP_FEATURES = 'width=1024,height=800,titlebar=no,toolbar=no,statusbar=no,directories=no,location=no';
const TYPES = ["PROGRAM","SEGMENTTYPE"]
const TYPES_F = ["BROADCAST", "STRAND", "MOVIE", "CLIP", "SEGMENT", "VISUALSEGMENT"]


function load(m) {
    head = $("head meta[name=mid]");
    if (m) {
        head.attr("content", m)
        history.pushState({}, null, m);
    }
    mid = head.attr("content");
    if (mid !== 'None') {
        $.getJSON('mediaobject/' + mid, function (data) {
            const mediaObject = new MediaObject(data);
            $("h1").text(mediaObject.mid + ":" + mediaObject.getMainTitle());
            const nowPlayable = mediaobjects.nowPlayable(mediaObject);
            if (nowPlayable.length === 0) {
                $("#playable").text("NIET AFSPEELBAAR");
            } else {
                $("#playable").text(nowPlayable.toString());
            }
        });
    }
}
$(function() {
    load();
    $("#select").click(function () {
        media.select(
            function (value) {
                load(value.mid);
            }, {
                mediaType: TYPES,
                returnValue: "data"
            }
        );
    });
    let popup;
    $("#eoselect").click(function () {
        const joined = TYPES_F.join("&types=")
        popup = window.open(POMS_LOOKUP_URL + '/?types=' + joined + '&limit=1', '', POPUP_FEATURES);
    });

    window.addEventListener( 'message', onMessage, false );

    function onMessage(event) {
        const origin = event.origin || event.originalEvent.origin;

        // Check if the message is coming from POMS Lookup and if the message data contains an `items` property
        if (origin === POMS_LOOKUP_URL && event.data && event.data.items) {
            load(event.data.items.map(function (item) {
                return item.mid;
            })[0]);

            // Close the popup
            popup.close();
        }
    }
});


