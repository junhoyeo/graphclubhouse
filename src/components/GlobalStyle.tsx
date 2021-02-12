import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    font-family: 'Nunito', sans-serif;
  }

  body {
    margin: 0;
  }
`;

export default GlobalStyle;
