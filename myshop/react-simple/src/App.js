import React from 'react';
import ShopList from './shoplist/ShopList';


function App() {
  const shoplists = [
    {id: 1, completed: false, title: 'Купить хлеб'},
    {id: 2, completed: false, title: 'Купить сыр'},
    {id: 3, completed: false, title: 'Купить творог'},
  ]


  return (
    <div className='wrapper'>
    <h1>Hello world</h1>
    <ShopList shoplists={shoplists}/>
    </div>
  );
}

export default App;
