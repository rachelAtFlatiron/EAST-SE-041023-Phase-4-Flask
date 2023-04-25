// 📚 Review With Students:
    // Request response cycle
    //Note: This was build using v5 of react-router-dom
import { Route, Switch } from 'react-router-dom'
import {useEffect, useState} from 'react'
import Home from './components/Home'
import ProductionForm from './components/ProductionForm'
import ActorForm from './components/ActorForm'
import Navigation from './components/Navigation'
import ProductionDetail from './components/ProductionDetail'
import NotFound from './components/NotFound'
import ActorContainer from './components/ActorContainer'
import ActorDetail from './components/ActorDetail'

function App() {
  const [productions, setProductions] = useState([])
  const [actors, setActors] = useState([])

  useEffect(() => {
    fetch('/productions')
    .then(res => res.json())
    .then(setProductions)
    fetch('/actors')
    .then(res => res.json())
    .then(setActors)
  },[])

  // Bonus: async and await version
  // useEffect(async () => {
  //   const res = await fetch('/productions')
  //   const productions = await res.json()
  //   setProductions(productions)
  // },[])

  const addProduction = (production) => setProductions(current => [...current,production])

  return (
    <div className="App light">
    <Navigation/>
      <Switch>
        <Route path='/actors/new'>
          <ActorForm />
        </Route>
        <Route  path='/productions/new'>
          <ProductionForm addProduction={addProduction}/>
        </Route>
        <Route path='/productions/:id'>
            <ProductionDetail />
        </Route>
        <Route path='/actors/:id'>
          <ActorDetail />
        </Route>
        <Route path='/actors'>
          <ActorContainer actors={actors} />
        </Route>
        
        <Route exact path='/'>
          <Home  productions={productions}/>
        </Route>
        <Route>
          <NotFound />
        </Route>
      </Switch>
    </div >
  )
}

export default App

