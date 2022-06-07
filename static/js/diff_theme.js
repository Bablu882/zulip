import $ from "jquery";

import {localstorage} from "./localstorage";
import {page_params} from "./page_params";

export function enable() {
    $("body").removeClass("color-scheme-automatic").addClass("diff-theme");

    if (page_params.is_spectator) {
        const ls = localstorage();
        ls.set("spectator-theme-preference", "diff");
    }
}

export function disable() {
    $("body").removeClass("color-scheme-automatic").removeClass("diff-theme");

    if (page_params.is_spectator) {
        const ls = localstorage();
        ls.set("spectator-theme-preference", "light");
    }
}

export function default_preference_checker() {
    $("body").removeClass("diff-theme").addClass("color-scheme-automatic");
}
