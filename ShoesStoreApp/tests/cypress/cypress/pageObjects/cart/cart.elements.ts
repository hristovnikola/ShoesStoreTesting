export class CartElements {
    static get ElementsCart() {
        return {
            getItemQuantity: () => cy.get('.item_quantity'),
            getPrice: () => cy.get('.shoes_cart_price'),
            getOrderItemPrice: () => cy.get('.order_item_price'),
            getOrderPrice: () => cy.get('.total_order_price'),
            getIncreaseQuantityButton: () => cy.get('.inc'),
            getDecreaseQuantityButton: () => cy.get('.dec'),
            getDeleteOrderItemButton: () => cy.get('.delete_cart_item'),
            getDeleteWholeOrderButton: () => cy.get('#delete_order'),
            getCheckoutButton: () => cy.get('#checkout_button'),
        }
    }
}