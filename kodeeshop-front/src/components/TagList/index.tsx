import React from 'react';
import './TagList.scss';
import Icon from '../Icon';

interface TagListProps {
  title: string;
  tags: {
    id: number;
    name: string;
    slug: string;
    createdAt: string;
    updatedAt: string;
  }[];
}

const TagList = (props: TagListProps) => {
  const {title, tags} = props;
  return (
    <div className="tag-list">
      <div className="tag-list__title">{title}</div>
      <ul className="tag-list__list">
        {tags.map((tag) => {
          return (
            <li key={tag.id} className="tag-list__list__item">
              <a href={tag.slug}>
                <span>{tag.name}</span>
              </a>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default TagList;
