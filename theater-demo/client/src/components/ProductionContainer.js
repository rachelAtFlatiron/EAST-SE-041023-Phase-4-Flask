import ProductionCard from './ProductionCard'


function ProductionContainer({productions}) {

    return (
     <section>
         <ul className='cards'>
             {productions.map(production => <ProductionCard  key={production.id} production={production}  />)}
         </ul>
     </section>
    )
  }
  
export default ProductionContainer
