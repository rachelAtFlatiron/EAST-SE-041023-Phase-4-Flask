import ActorCard from './ActorCard'

function ActorContainer({ actors }) {
  return (
    <section>
         <ul className='cards'>
             {actors.map(actor => <ActorCard  key={actor.id} actor={actor}  />)}
         </ul>
     </section>
  )
}

export default ActorContainer