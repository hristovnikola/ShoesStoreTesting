export class LoginElements {
    static get ElementsLogin() {
        return {
            getLoginNavButton: () => cy.get('#login_button'),
            getUsernameField: () => cy.get('#login_field'),
            getPasswordField: () => cy.get('#password_field'),
            getLoginSubmitButton: () => cy.get('#log_in_button'),
            getBodyText: () => cy.get('body').invoke('text')
        }
    }
}


