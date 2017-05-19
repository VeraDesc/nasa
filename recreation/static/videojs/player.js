(function($){

    var player;

    $(function () {
        var overlay = $("<div id='player-overlay'></div>");
        $("body").append(overlay);
        player = videojs('videojs');
        player.hide();
    });

    $.fn.extend({

        videoPlayer: function(options) {

            var defaults = {
                top: 100,
                overlay: 0.5,
                width: 800,
                height: 560,
                closeButton: null,
                youtube: 'FyEcBP98CSk'
            }

            options =  $.extend(defaults, options);

            return this.each(function() {
                var surface = this;
                var source = "https://www.youtube.com/watch?v=" + options.youtube;

                player.show();
                player.autoplay(true);
                player.height(options.height + 'px');
                player.width(options.width + 'px');
                player.src({
                    'src': source,
                    "type": "video/youtube"
                });
                player.play();

                $('#player-overlay').css({ 'display' : 'block', opacity : 0 });
                $('#player-overlay').fadeTo(200,options.overlay);

                $(document).keydown(function(e) {
                    if (e.keyCode == 27) { // escape key maps to keycode `27`
                        close_player();
                    }
                });
                $('#player a.close-img').click(close_player);

                $(surface).css({
                    'display' : 'block',
                    'position' : 'fixed',
                    'width': options.width,
                    'height': options.height,
                    'opacity' : 0,
                    'z-index': 11000,
                    'left' : 50 + '%',
                    'margin-left' : -(options.width / 2) + "px",
                    'top' : options.top + "px"

                });

                $(surface).fadeTo(2000,1);

                function close_player(){
                    $("#player-overlay").fadeOut(200);
                    $(surface).css({ 'display' : 'none' });
                    player.pause();
                    player.hide();
                }
            });

        }
    });

})(jQuery);
