import react from 'react'

const ProductsRow = ({name, category, price, summary, author, photo, content}) => {
    return(
        <tr>
                    <td>{name}</td>
                    <td>{category}</td>
                    <td>{price}</td>
                    <td>{summary}</td>
                    <td>{author}</td>
                    <td>{photo}</td>
                    <td>{content}</td>
                        <button className = "btn btn-outline-UPDATE btn-sm ml-1 mr-2">UPDATE</button>
                        <button className = "btn btn-outline-CATEGORY btn-sm ml-1 mr-2">CATEGORIA</button>
                        <button className = "btn btn-outline-DELETE btn-sm ml-1 mr-2">Eliminar</button>

        </tr>

    )
}

export default ProductsRow