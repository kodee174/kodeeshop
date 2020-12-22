import React from 'react';
import './BannerBox.scss';

interface BannerBoxProps {
  variant: 1 | 2 | 3;
  image: string;
  title: string;
  content: string;
}

const defaultProps = {
  variant: 1,
};

const BannerBox = (props: BannerBoxProps) => {
  const {variant, image, title, content} = props;
  return (
    <div className="banner-box">
      <img className="banner-box__image" src={image} alt={title} />
      {variant === 1
        ? [
            <div key="bannerBoxText" className="banner-box__text--variant-1">
              <div className="banner-box__text__title">{title}</div>
              <div className="banner-box__text__content">{content}</div>
            </div>,
            <button key="bannerBoxDiscover" className="banner-box__discover">
              Khám phá ngay
            </button>,
          ]
        : null}
      {variant === 2 ? (
        <div className="banner-box__text--variant-2">
          <div className="banner-box__text__title">{title}</div>
          <div className="banner-box__text__content">{content}</div>
        </div>
      ) : null}
      {variant === 3 ? (
        <div className="banner-box__text--variant-3">
          <div className="banner-box__text__title">{title}</div>
          <div className="banner-box__text__content">{content}</div>
        </div>
      ) : null}
    </div>
  );
};

BannerBox.defaultProps = defaultProps;

export default BannerBox;
