/* @odoo-module */

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { session } from "@web/session";
import { user } from "@web/core/user";
import { useService } from "@web/core/utils/hooks";

export class LanguageSwitcher extends Component {
    static props = [];
    static template = "display_language_switcher.LanguageSwitcher";
    setup() {
        this.state = useState({languages: [], lang_code: user.lang.replace('-', '_')});
        this.orm = useService("orm");
        this.getLanguages();
    }
    async getLanguages() {
        this.state.languages = await this.orm.call("res.lang", "get_installed");
    }
    async onChangeLanguage(lang_code) {
        this.state.lang_code = lang_code;
        await this.orm.call("res.users", "write", [[user.userId], {lang: this.state.lang_code}]);
        location.reload();
    }
}

registry.category("systray").add("display_language_switcher.LanguageSwitcher", { Component: LanguageSwitcher }, { sequence: 15 });
