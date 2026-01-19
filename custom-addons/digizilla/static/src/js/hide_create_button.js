odoo.define('digizilla.hide_create_button', function (require) {
    "use strict";

    var ListController = require('web.ListController');

    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                // Hide "Create" button in list/kanban views
                this.$buttons.find('.o_list_button_add').hide();
            }
        },
    });
});
