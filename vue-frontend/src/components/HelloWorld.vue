<template>
  <div class="hello">
    <h1>Web Scrapper</h1>

    <div class="search-container">
      <input type="text" id="url" placeholder="Web Page URL" v-model="inputUrl">
      <button @click="handleSubmit">Submit</button>
      <button @click="generatePDF()">Generate PDF</button>
    </div>


    <div class="search-container">
      <input type="text" id="query" placeholder="Search in content" v-model="query">
      <button @click="highlight">Search Text</button>
      <button @click="reset">Reset</button>
    </div>

    <vue-html2pdf :show-layout="false" :float-layout="true" :enable-download="true" :preview-modal="true"
      :paginate-elements-by-height="1400" filename="nightprogrammerpdf" :pdf-quality="2" :manual-pagination="false"
      pdf-format="a4" :pdf-margin="10" pdf-orientation="portrait" pdf-content-width="800px" @progress="onProgress($event)"
      ref="html2Pdf">
      <section slot="pdf-content">
        <div v-html="this.renderHtml"></div>
      </section>
    </vue-html2pdf>

    <div v-html="this.renderHtml" v-if="renderHtml"></div>
  </div>
</template>

<script>
import axios from 'axios';
import VueHtml2pdf from "vue-html2pdf";

export default {
  name: 'HelloWorld',
  data() {
    return {
      inputUrl: "",
      html: null,
      query: null,
      renderHtml: null,
    }
  },
  methods: {
    async handleSubmit() {
      let res = await axios.post(`http://127.0.0.1:8000/scrapper`, { url: this.inputUrl });
      this.html = res?.data
      this.renderHtml = res?.data
    },
    onProgress(event) {
      console.log(`Processed: ${event} / 100`);
    },
    hasGenerated() {
      alert("PDF generated successfully!");
    },
    generatePDF() {
      this.$refs.html2Pdf.generatePdf();
    },

    highlight() {
      if (!this.query) {
        return this.html;
      }

      const updatedHTML = this.html.replace(new RegExp(this.query, "gi"), match => {
        return '<span style="background: yellow"">' + match + '</span>';
      });

      this.renderHtml = updatedHTML
    },
    reset() {
      this.renderHtml = this.html
    }
  },
  components: {
    VueHtml2pdf,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.search-container {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 16px;
}

input {
  font-size: 16px;
  font-family: inherit;
  padding: 8px;
  background-color: #fff;
  border: 1px solid #8b8a8b;
  border-radius: 4px;
  transition: 180ms box-shadow ease-in-out;
  width: 100%;
  max-width: 700px;
}

input:focus {
  outline: 3px solid transparent;
}

button {
  border-radius: 4px;
  background-color: #f4511e;
  border: none;
  color: white;
  padding: 10px 32px;
  text-align: center;
  font-size: 16px;
  transition: 0.3s;
  display: inline-block;
  text-decoration: none;
  cursor: pointer;
}
</style>
