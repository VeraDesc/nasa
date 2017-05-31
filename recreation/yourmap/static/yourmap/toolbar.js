
var CenteringAction = L.ToolbarAction.extend({
    options: { toolbarIcon: { html: '&#10752;', tooltip: 'centering the map' } },
    addHooks: function () {
        L.DomUtil.disableTextSelection();
        L.DomUtil.addClass(this._icon,'active');
        this.toolbar.toggleDragging();

        var self = this;
        this.toolbar.mapOnceClick(function (ev) {
            var map = this._map; // Note: context is the toolbar
            L.DomEvent.stopPropagation(ev);
            map.setView(ev.latlng, map.getZoom());
            self.disable();
        });
    },
    removeHooks: function () {
        L.DomUtil.removeClass(this._icon,'active');
        this.toolbar.toggleDragging();
    }
});

var MoveToolbar = L.ToolbarAction.extend({
    options: { toolbarIcon: { html: '&#10561;', tooltip: 'move toolbar to another corner' } },
    addHooks: function () {
        this.toolbar.switchPosition();
    }
});

var Toolbar = L.Toolbar.Control.extend({
    switchPosition: function () {
        var pos = {
            topright: "bottomright",
            bottomright: "bottomleft",
            bottomleft: "topleft",
            topleft: "topright"
        };

        var control = this._control;
        var newpos = pos[control.getPosition()];
        control.setPosition(newpos);
    },
    toggleDragging: function () {
        var map = this._map;
        if(map.dragging.enabled()) {
            map.dragging.disable();
        }
        else {
            map.dragging.enable();
        }
    },
    mapOnceClick: function (callback) {
        var map = this._map;
        map.getContainer().focus();
        map.once('click', callback, this);
    }
});

function showToolbar(map) {
    var toolbar = new Toolbar({
        position: "topright",
        actions: [
            MoveToolbar,
            CenteringAction,
        ]
    }).addTo(map);

}
