export class ShoesElements{
    static get ElementsShoes(){
        return {
            getShoesNavButton: () => cy.get('#shoes_button'),
            getAddShoesButton: () =>  cy.get('#add_shoes_btn'),
            getDetailsButtons: () => cy.get('.details_button'),
            getEditButton: () => cy.get('#edit_button'),
            getDeleteButton: () => cy.get('#delete_button'),
            getAddToCartButton: () => cy.get('#add_to_cart_button'),
            getBackToShoesButton: () => cy.get('#back_to_shoes'),
            getBodyText: () => cy.get('body').invoke('text'),
            getShoesSizeInput: () => cy.get('input[name="selected_size"]')
        }
    }

    static get AddAndEditShoesElements(){
        return {
            getNameField: () => cy.get('#id_name'),
            getPriceField: () => cy.get('#id_price'),
            getDescriptionField: () => cy.get('#id_description'),
            getAvailableSizesField: () => cy.get('#id_size'),
            getBrandField: () => cy.get('#id_brand'),
            getTypeField: () => cy.get('#id_type'),
            getColorField: () => cy.get('#id_color'),
            getImageField: () => cy.get('#id_image'),
            getSubmitAddingOrEditingShoesButton: () => cy.get('#add_edit_shoes_submit')
        }
    }
}