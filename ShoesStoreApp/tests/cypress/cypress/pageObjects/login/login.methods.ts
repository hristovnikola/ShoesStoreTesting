import {LoginElements} from "./login.elements";

export class LoginMethods {
    login(username: string, password: string) {
        LoginElements.ElementsLogin.getUsernameField().type(username);
        LoginElements.ElementsLogin.getPasswordField().type(password);
        LoginElements.ElementsLogin.getLoginSubmitButton().click();
    }

    navigateToLoginPage() {
        LoginElements.ElementsLogin.getLoginNavButton().click();
    }

    verifyUsernameExistsOnPage(username: string) {
        LoginElements.ElementsLogin.getBodyText().should('contain', username);
    }

    verifyUsernameDoesNotExistsOnPage(username: string) {
        LoginElements.ElementsLogin.getBodyText().should('not.contain', username);
    }
}