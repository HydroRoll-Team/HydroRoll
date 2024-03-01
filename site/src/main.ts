/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */


// Components
import App from './App.vue'

// Composable
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

import './assets/main.css'
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// highlights
import hljs from 'highlight.js';

VMdPreview.use(githubTheme, {
  Hljs: hljs,
});




const app = createApp(App)
app.use(VMdPreview)
app.use(ElementPlus)
registerPlugins(app)
app.mount('#app')
