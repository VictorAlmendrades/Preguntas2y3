import react, {useEffect, useContext} from 'react'
import {Table} from 'react-bootstrap'
import {ProductContext} from '../ProductContext'
import ProductsRow from './ProductsRow'

const ProductsTable = () => {
    const [products, setProducts] = useContext(ProductContext)

    useEffect(() =>{
        fetch("http://127.0.0.1:8000")
        .then(resp=>{
            return resp.json();
        }).then(results =>{
            console.log(results)
            setProducts({"data" : [...results.data]})
        }) 
    })
    return(
        <div>
            <Table striped bordered hover>
            <thead>
                <tr>
                    <th>name</th>
                    <th>category</th>
                    <th>price</th>
                    <th>summary</th>
                    <th>author</th>
                    <th>photo</th>
                    <th>content</th>

                 </tr>
            </thead>
            <tbody>
                { products.data.map((product) =>(
                    <ProductsRow>
                        name = {product.name}
                        category = {product.category}
                        price = {product.price}
                        summary = {product.summary}
                        author = {product.author}
                        photo = {product.photo}
                        content = {product.content}
                    </ProductsRow>
                ))}
            </tbody>
            </Table>
        </div>
    );
}

export default ProductsTable;