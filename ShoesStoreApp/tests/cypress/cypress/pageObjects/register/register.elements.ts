export class RegisterElements {
    static get ElementsRegister() {
        return {
            getLoginNavButton: () => cy.get('#login_button'),
            getRegisterBtnInLoginForm: () => cy.get('#register_in_form_login'),
            getUsernameField: () => cy.get('#id_username'),
            getEmailField: () => cy.get('#id_email'),
            getPasswordField: () => cy.get('#id_password1'),
            getConfirmPasswordField: () => cy.get('#id_password2'),
            getRegisterSubmitButton: () => cy.get('#register_button'),
            getBodyText: () => cy.get('body').invoke('text')
        }
    }
}