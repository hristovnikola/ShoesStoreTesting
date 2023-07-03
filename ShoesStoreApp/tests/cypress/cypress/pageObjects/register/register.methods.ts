import {RegisterElements} from "./register.elements";

export class RegisterMethods{
    register(username: string, email: string, password: string, repeat_password: string){
        RegisterElements.ElementsRegister.getUsernameField().type(username);
        RegisterElements.ElementsRegister.getEmailField().type(email);
        RegisterElements.ElementsRegister.getPasswordField().type(password);
        RegisterElements.ElementsRegister.getConfirmPasswordField().type(repeat_password);
        RegisterElements.ElementsRegister.getRegisterSubmitButton().click()
    }

    navigateToLoginPage(page:string){
        cy.visit(page);
        RegisterElements.ElementsRegister.getLoginNavButton().click();
    }

    navigateToRegisterPage() {
        RegisterElements.ElementsRegister.getRegisterBtnInLoginForm().click();
    }
    verifyUsernameExistsOnPage(username: string) {
    // RegisterElements.RegisterElements.getBodyText().should('contain', username);
  }
}