const mediaobjects = nl_vpro_domain_media_MediaObjects;

mid = $("head meta[name=mid]").attr("content")
if (mid !== 'None') {
    $.getJSON('mediaobject/' + mid, function (data) {
        const mediaObject = new MediaObject(data);
        if (mediaObject !== 'None') {
            $("h1").text(mediaObject.mid + ":" + mediaObject.getMainTitle());
            console.log(mediaobjects.nowPlayable(mediaObject));
            $("#playable").text(mediaobjects.nowPlayable(mediaObject).toString());
        }
        $("#select").click(function () {
            document.getElementById('select').onclick = function () {
                media.select(
                    function (value) {
                        document.location = value.mid;
                    }, {
                        mediaType: "BROADCAST",
                        returnValue: "data"
                    }
                );
            };

        });

    });
}

