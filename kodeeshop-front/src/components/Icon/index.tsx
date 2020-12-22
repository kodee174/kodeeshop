import React from 'react';
import {FontAwesomeIcon, FontAwesomeIconProps} from '@fortawesome/react-fontawesome';
import {library} from '@fortawesome/fontawesome-svg-core';
import {fas} from '@fortawesome/free-solid-svg-icons';
import {fab} from '@fortawesome/free-brands-svg-icons';

library.add(fas, fab);

interface IconProps {
  icon: string[];
  size: string;
  rotation: number;
  flip: string;
}

const defaultProps = {
  size: 'xs',
  rotation: 0,
  flip: null,
};

const Icon = (props: IconProps) => {
  const {icon, size, rotation, flip} = props as FontAwesomeIconProps;
  return <FontAwesomeIcon icon={icon} size={size} rotation={rotation} flip={flip} />;
};

Icon.defaultProps = defaultProps;

export default Icon;
