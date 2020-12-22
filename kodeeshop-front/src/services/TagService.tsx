import React from 'react';
import humps from 'humps';
import Path from '../configs/path';

const TagService = {
  getTags: async () => {
    const data = await fetch(`${Path.BACK_URL}/api/tags`);
    return data.json();
  },
};

export default TagService;
