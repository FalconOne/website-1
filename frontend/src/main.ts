import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createMetaManager } from 'vue-meta'

import './index.css'

const app = createApp(App)
app.use(router)
app.use(createMetaManager())

await router.isReady()
app.mount('#app')
