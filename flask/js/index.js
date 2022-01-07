const mediaobjects = nl_vpro_domain_media_MediaObjects;
const POMS_LOOKUP_URL = 'https://pomslookup.eo.nl';
const POPUP_FEATURES = 'width=1024,height=800,titlebar=no,toolbar=no,statusbar=no,directories=no,location=no';
const TYPES = ["PROGRAM","SEGMENTTYPE"]
const TYPES_F = ["BROADCAST", "STRAND", "MOVIE", "CLIP", "SEGMENT", "VISUALSEGMENT"]


function load(m) {
    const head = $("head meta[name=mid]");
    if (m) {
        head.attr("content", m)
        history.pushState({}, null, m);
    }
    var mids = JSON.parse(localStorage.getItem("mids"));
    if (mids == null) {
        mids = [];
        $("#examples li a").each(function(li) {
            mids.push($(this).text());
            }
        );
    }
    function pushUnless(array, element) {
        if ($.inArray(element, array) < 0) {
            array.push(element);
        }
    }
    mid = head.attr("content");
    if (mid !== 'None') {
        pushUnless(mids, mid);
        localStorage.setItem("mids", JSON.stringify(mids));
        $.getJSON('mediaobject/' + mid, function (data) {
            const mediaObject = new MediaObject(data);
            $("h1").text(mediaObject.mid + ":" + mediaObject.getMainTitle());
            const nowPlayable = mediaobjects.nowPlayable(mediaObject);
            if (nowPlayable.length === 0) {
                $("#playable").text("NIET AFSPEELBAAR");
            } else {
                $("#playable").text(nowPlayable.toString());
            }
            $("#ranges").text(JSON.stringify(mediaobjects.playableRanges(mediaObject)))
        });
    }
    $(mids).each(function(i, value) {
        if ($("#examples li a:contains(" + value + ")").length === 0) {
            $("#examples").append("<li><a href='" + value + "'>" + value + "</a></li>");
        }
    })
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


