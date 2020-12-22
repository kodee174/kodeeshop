import React from 'react';
import './CollectionList.scss';

interface CollectionListProps {
  image: string;
  title: string;
  collections: {
    idCollection: number;
    current?: boolean;
    title: string;
  }[];
}

const CollectionList = (props: CollectionListProps) => {
  const {image, title, collections} = props;
  return (
    <div className="collection-list">
      <img className="collection-list__image" src={image} alt={title} />
      <div className="collection-list__title">{title}</div>
      <ul className="collection-list__list">
        {collections.map((collection, index) => {
          return collection.current ? (
            <li
              key={`collection-${collection.idCollection}`}
              className="collection-list__list__item collection-list__list__item--current"
            >
              {collection.title}
            </li>
          ) : (
            <li key={`collection-${collection.idCollection}`} className="collection-list__list__item">
              {collection.title}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default CollectionList;
