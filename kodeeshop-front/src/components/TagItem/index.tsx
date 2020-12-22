import React from 'react';
import './TagItem.scss';

interface TagItemProps {
  slug: string;
  image: string;
  title: string;
}

const TagItem = (props: TagItemProps) => {
  const {slug, image, title} = props;
  return (
    <div className="tag-item">
      <a className="tag-item__link" href={slug}>
        <img className="tag-item__link__image" src={image} alt={title} />
        <h3 className="tag-item__link__title">{title}</h3>
      </a>
    </div>
  );
};

export default TagItem;
