const mediaobjects = nl_vpro_domain_media_MediaObjects;
const POMS_LOOKUP_URL = 'https://pomslookup.eo.nl';

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
            if (mediaObject !== 'None') {
                $("h1").text(mediaObject.mid + ":" + mediaObject.getMainTitle());
                //console.log(mediaobjects.nowPlayable(mediaObject));
                $("#playable").text(mediaobjects.nowPlayable(mediaObject).toString());
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
                mediaType: "BROADCAST",
                returnValue: "data"
            }
        );
    });
    var popup;
    $("#eoselect").click(function () {
        popup = window.open(POMS_LOOKUP_URL + '/?types=BROADCAST&limit=1', 'POMS_Lookup');
    });

    window.addEventListener( 'message', onMessage, false );

    function onMessage(event) {
        var origin = event.origin || event.originalEvent.origin;

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


