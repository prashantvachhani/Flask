from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sneat/html/index.html') 

@app.route('/cointener')
def contener():
    return render_template('sneat/html/layouts-container.html')

@app.route('/layouts-fluid')
def layouts_fluid():
    return render_template('sneat/html/layouts-fluid.html')

@app.route('/layouts-without-menu')
def without_menu():
    return render_template('sneat/html/layouts-without-menu.html')

@app.route('/layouts-without-navbar')
def without_nav():
    return render_template('sneat/html/layouts-without-navbar.html')

@app.route('/blank')
def layoute_blank():
    return render_template('sneat/html/layouts-blank.html')

@app.route('/fluid')
def fluid():
    return render_template('sneat/html/layouts-fluid.html') 

@app.route('/layouts-blank')
def layout_blank():
    return render_template('sneat/html/layouts-blank.html')

# Page Routing
@app.route('/pages-account-settings-account')
def pages_account():
    return render_template('sneat/html/pages-account-settings-account.html')

@app.route('/pages-account-settings-connections')
def page_connection():
    return render_template('sneat/html/pages-account-settings-connections.html')

@app.route('/pages-account-settings-notifications')
def page_notification():
    return render_template('sneat/html/pages-account-settings-notifications.html')

@app.route('/auth-login-basic')
def page_login():
    return render_template('sneat/html/auth-login-basic.html')

@app.route('/auth-register-basic')
def page_Rejister():
    return render_template('sneat/html/auth-register-basic.html')

@app.route('/auth-forgot-password-basic')
def page_forgot_passworld():
    return render_template('sneat/html/auth-forgot-password-basic.html')

@app.route('/pages-misc-error')
def page_misc_error():
    return render_template('sneat/html/pages-misc-error.html')

@app.route('/pages-misc-under-maintenance')
def page_misc_maintaince():
    return render_template('sneat/html/pages-misc-under-maintenance.html')


# Component

@app.route('/cards-basic')
def cards():
    return render_template('sneat/html/cards-basic.html')

# User Interface
@app.route('/ui-accordion')
def according():
    return render_template('sneat/html/ui-accordion.html')

@app.route('/ui-alerts')
def ui_alert():
    return render_template('sneat/html/ui-alerts.html')

@app.route('/ui-badges')
def ui_badge():
    return render_template('sneat/html/ui-badges.html')

@app.route('/ui-buttons')
def ui_button():
    return render_template('sneat/html/ui-buttons.html')

@app.route('/ui-carousel')
def  ui_cursor():
    return render_template('sneat/html/ui-carousel.html')

@app.route('/ui-collapse')
def ui_collapse():
    return render_template('sneat/html/ui-collapse.html')

@app.route('/ui-dropdowns')
def ui_dropdowun():
    return render_template('sneat/html/ui-dropdowns.html')

@app.route('/ui-footer')
def ui_footer():
    return render_template('sneat/html/ui-footer.html')

@app.route('/ui-list-groups')
def ui_list_group():
    return render_template('sneat/html/ui-list-groups.html')

@app.route('/ui-modals')
def ui_model():
    return render_template('sneat/html/ui-modals.html')

@app.route('/ui-navbar')
def ui_navbar():
    return render_template('sneat/html/ui-navbar.html')

@app.route('/ui-offcanvas')
def ui_offcanvas():
    return render_template('sneat/html/ui-offcanvas.html')

@app.route('/ui-pagination-breadcrumbs')
def ui_oagination_breadcrumbs():
    return render_template('sneat/html/ui-pagination-breadcrumbs.html')

@app.route('/ui-progress')
def ui_progress():
    return render_template('sneat/html/ui-progress.html')

@app.route('/ui-spinners')
def ui_spinner():
    return render_template('sneat/html/ui-spinners.html')

@app.route('/ui-tabs-pills')
def ui_tabs_pills():
    return render_template('sneat/html/ui-tabs-pills.html')

@app.route('/ui-toasts')
def ui_toasts():
    return render_template('sneat/html/ui-toasts.html')

@app.route('/ui-tooltips-popovers')
def ui_tooltips():
    return render_template('sneat/html/ui-tooltips-popovers.html')

@app.route('/ui-typography')
def ui_typography():
    return render_template('sneat/html/ui-typography.html')


# Extended Command Routing

@app.route('/extended-ui-perfect-scrollbar')
def extended_ui_perfect_scrollbar():
    return render_template('sneat/html/extended-ui-perfect-scrollbar.html')

@app.route('/extended-ui-text-divider')
def extended_ui_text_divider():
    return render_template('sneat/html/extended-ui-text-divider.html')

@app.route('/icons-boxicons')
def icons_boxicons():
    return render_template('sneat/html/icons-boxicons.html')

# Forms & Tables Routing

@app.route('/forms-basic-inputs')
def forms_basic_inputs():
    return render_template('sneat/html/forms-basic-inputs.html')

@app.route('/forms-basic-inputs')
def forms_basic_input():
    return render_template('sneat/html/forms-basic-inputs.html')

@app.route('/forms-input-groups')
def forms_input_group():
    return render_template('sneat/html/forms-input-groups.html')

@app.route('/form-layouts-vertical')
def form_layouts_vertical():
    return render_template('sneat/html/form-layouts-vertical.html')

@app.route('/form-layouts-horizontal')
def form_layouts_horizontal():
    return render_template('sneat/html/form-layouts-horizontal.html')

# Tables Routing

@app.route('/tables-basic')
def table_basic():
    return render_template('sneat/html/tables-basic.html')

# Log Out Routing
@app.route('/auth-login-basic')
def auth_login_basic():
    return render_template('sneat/html/auth-login-basic.html')

# Redirect Route
@app.route('/<data>')
def handle_number(data):
    try:
        # Try converting to int
        num = int(data)
        return f"<h2>Your integer number is: {num}</h2>"
    except ValueError:
        # If not a valid integer, redirect to /blank
        return redirect(url_for('page_misc_error'))


if __name__ == '__main__':
    app.run(debug=True)