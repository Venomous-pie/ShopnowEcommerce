// eslint.config.js
import vue from 'eslint-plugin-vue';

export default [
  {
    files: ['**/*.js', '**/*.vue'],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: 'module',
      globals: { browser: true, node: true },
    },
    plugins: { vue },
    rules: {
      // Add custom rules here
    },
  },
  {
    files: ['**/*.vue'],
    plugins: { vue },
    extends: ['plugin:vue/vue3-recommended'],
  },
];
