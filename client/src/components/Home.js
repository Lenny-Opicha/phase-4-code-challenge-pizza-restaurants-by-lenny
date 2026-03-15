import { useEffect, useState } from "react";

function Home() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch("/pizzas") // works if proxy is set in package.json
      .then((res) => res.json())
      .then((data) => setPizzas(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>All Pizzas</h1>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            {pizza.name} - {pizza.toppings} (${pizza.price})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home; 