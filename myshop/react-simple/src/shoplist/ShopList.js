import React from 'react';
import PropTypes from 'prop-types';
import ShopListItem from './ShopListItem';


const styles = {
  ul: {
    listStyle: 'none',
    margin: 0,
    padding: 0,
  }
}

function ShopList(props) {
  return(
    <ul style={styles.ul}>
    { props.shoplists.map((shoplist, index) => {
      return <ShopListItem shoplist={shoplist} key={shoplist.id} index={index+1}/>
    }) }
    </ul>
  )
}

export default 
