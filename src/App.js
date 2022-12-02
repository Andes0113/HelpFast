import React from 'react';
import { ChakraProvider } from '@chakra-ui/react'
import Header from './components/Header';
import About from './pages/About';
import Matches from './pages/Matches';
import Match from './pages/Match';
import Settings from './pages/Settings';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  return (
    <ChakraProvider>
      <Router basename='/'>
        <Header />
        <Routes>
          <Route path="/" exact element={<About />}/>
          <Route path="/match" element={<Match />}/>
          <Route path="/matches" element={<Matches />}/>
          <Route path="/settings" element={<Settings />}/>
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;