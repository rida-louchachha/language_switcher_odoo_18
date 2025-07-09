Display Language Switcher
=========================

A simple Odoo 18.0 module to enable users to switch the UI language directly from the top bar (systray) with a clean, configurable interface.

Overview
--------

This module adds a **language switcher icon** to the top-right menu bar of the Odoo interface, allowing users to change the language on-the-fly without navigating through settings.

It also provides the ability to customize background visuals using CSS and embeds support for beautiful typography and imagery.

Features
--------

- 🌐 Add a systray item for language switching
- 🎨 Customize background with a SCSS stylesheet
- 🖼️ Bundle custom image and fonts (Poppins)
- 🧩 Minimal configuration – ready to deploy
- 🔤 Supports multilingual Odoo environments

Installation
------------

1. Clone or download this repository and place the folder in your Odoo `addons` directory.

   .. code-block:: bash

       git clone https://github.com/yourusername/display_language_switcher.git

2. Restart your Odoo server.
3. Activate developer mode in Odoo.
4. Go to **Apps**, click **Update App List**, then search and install **Display Language Switcher**.

Usage
-----

Once installed, you will see a **language selector icon** in the top systray.

Click the icon to select your preferred language. The interface will reload in the selected language.

Preview
-------

.. image:: display_language_switcher/static/src/img/background.jpg
   :alt: Language Switcher Background
   :width: 600px

Technical Details
-----------------

- **SCSS**: Custom styling for login/background via `static/src/css/odoo_background.scss`
- **JS**: Language systray logic in `static/src/js/systray_item.js`
- **XML**: QWeb template for rendering the menu in `static/src/xml/systray_item.xml`
- **Fonts**: Includes Poppins font for enhanced UI consistency

Compatibility
-------------

- Odoo 18.0+
- Tested on Community Edition

Author & Maintainer
--------------------

- **Rida Louchachha**  
  GitHub: https://github.com/ridalouchachha2580  
  Email: ridalouchachha2580@gmail.com

License
-------

This module is licensed under the **MIT License**. See `LICENSE` file for full text.
