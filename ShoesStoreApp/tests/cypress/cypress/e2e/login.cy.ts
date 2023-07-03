import { LoginMethods } from "../pageObjects/login/login.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let index = new IndexMethods();
  const testData = require('../fixtures/login.json')

  testData.loginData.forEach((testcase: { username: string; password: string; }) => {
    it(testcase.username + ' should be able to login', () => {
      index.navigateToIndexPage('http://localhost:8000/index/');
      login.navigateToLoginPage();
      login.login(testcase.username, testcase.password);
      login.verifyUsernameExistsOnPage(testcase.username);
    })
  });
})