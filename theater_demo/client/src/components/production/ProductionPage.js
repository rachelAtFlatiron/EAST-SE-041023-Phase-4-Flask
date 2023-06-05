import React from 'react'
import ProductionContainer from './ProductionCard'

function ProductionPage({ productions }) {
  return (
    <ProductionContainer productions={productions} />
  )
}

export default ProductionPage