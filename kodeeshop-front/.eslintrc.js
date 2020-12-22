module.exports = {
    extends: [
      'airbnb-typescript',
      'airbnb/hooks',
      'plugin:@typescript-eslint/recommended',
      'plugin:jest/recommended',
      'prettier',
      'prettier/react',
      'prettier/@typescript-eslint',
      'plugin:prettier/recommended',
    ],
    plugins: ['@typescript-eslint', 'prettier', 'react', 'react-hooks', 'jest', 'jsx-a11y'],
    env: {
      browser: true,
      es6: true,
      jest: true,
    },
    globals: {
      Atomics: 'readonly',
      SharedArrayBuffer: 'readonly',
    },
    parser: '@typescript-eslint/parser',
    parserOptions: {
      ecmaFeatures: {
        jsx: true,
      },
      ecmaVersion: 6,
      sourceType: 'module',
      project: './tsconfig.json',
    },
    rules: {
      'prettier/prettier': ['error'],
      '@typescript-eslint/no-empty-interface': 0,
    },
  };