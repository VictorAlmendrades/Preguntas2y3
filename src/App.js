import react from 'react'
import {BrowserRouter as Router, Link, Route, Routes} from 'react-router-dom'
import NavBar from './components/NavBar'
import {ProductProvider} from './ProductContext'
import ProductsTable from './components/ProductsTable'

function App() {
  return (
  <div>
    <Router>
      <switch>
        <ProductProvider>
        <NavBar />
        <div className="row">
          <div className="col -sm-10 col-xm-12 mr-auto ml-auto mt-4 mb-4">
          <ProductsTable />
          </div>
        </div>
        </ProductProvider>
      </switch>
    </Router>
  </div>

  );
}

export default App;
