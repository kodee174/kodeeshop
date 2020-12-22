import React from 'react';
import humps from 'humps';
import Path from '../configs/path';

const CollectionService = {
  getCollections: async () => {
    const data = await fetch(`${Path.BACK_URL}/api/collections`);
    return data.json();
  },
};

export default CollectionService;
