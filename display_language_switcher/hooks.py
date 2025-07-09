# from odoo.modules.module import load_language
from odoo.api import Environment

def activate_languages(env: Environment):
    for code in ['en_US', 'fr_FR', 'ar_001']:
        # Check if already installed
        lang = env['res.lang'].search([('code', '=', code)], limit=1)
        if not lang.active:
                lang._activate_lang(code)
