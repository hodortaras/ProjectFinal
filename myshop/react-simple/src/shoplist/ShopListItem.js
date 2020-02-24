import React from 'react';

export default function ShopListItem({shoplist, index}) {
  return(
    <li><strong>{index}</strong>{shoplist.title}</li>
  )
}
