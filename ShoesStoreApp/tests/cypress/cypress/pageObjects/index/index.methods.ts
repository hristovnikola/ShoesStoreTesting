import {LoginElements} from "../login/login.elements";

export class IndexMethods{
    navigateToIndexPage(page: string) {
        cy.visit(page);
    }
    navigateToCertainPage(page: string){
        cy.visit(page);
    }
}