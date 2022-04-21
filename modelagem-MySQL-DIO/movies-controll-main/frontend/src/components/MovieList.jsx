import { useEffect, useState } from 'react';

const MovieList = () => {

    const [movies, setMovies] = useState([])
    
    useEffect(async () => {
        const url = "http://localhost:5000/movies";
        const res = await fetch(url);
        setMovies(await res.json());
    }, [])
    
    return(
            <table className="striped">
                <thead>
                <tr>
                    <th>Nome</th>
                    <th>Tipo</th>
                    <th>Episódios</th>
                    <th>Episódio atual</th>
                    <th>Visto por último</th>
                </tr>
                </thead>

                <tbody>
                {movies.map(movies => {
                    let type = movies.type_of === 0 ? 'Série' : 'Filme';
                    let formatDate = (movies.last_view).split('T', 1)

                    return(
                        <tr key={movies.id}>
                            <td>{movies.name_of}</td>
                            <td>{type}</td>
                            <td>{movies.total_ep}</td>
                            <td>{movies.atual_ep}</td>
                            <td>{formatDate}</td>
                        </tr>
                    )
                })}
                </tbody>
            </table>
    )
}

export default MovieList;
