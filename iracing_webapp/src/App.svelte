<script lang="ts">
  import { onMount } from "svelte";
  import { useForm, validators, HintGroup, Hint, email, required } from "svelte-use-form";


  const form = useForm();

  function handleLogin() {
    const email = document.querySelector('input[name="email"]');
    const password = document.querySelector('input[name="password"]');
    const data = { email, password };
    console.log(data);
    fetch("https://members-ng.iracing.com/auth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((res) => {
        if (res.status === 200) {
          alert("Login successful");
        } else {
          alert("Login failed");
        }
      })
      .catch(err => {
        console.log(err);
      });
  }
</script>

<main>
  <h1>Login Page</h1>

  <div class="loginform">
    <form use:form>
      <div>
      <input type="email" name="email" use:validators={[required, email]} />
      <HintGroup for="email">
        <Hint on="required">This is a mandatory field</Hint>
        <Hint on="email" hideWhenRequired>Email is not valid</Hint>
      </HintGroup>
    </div>
    <div>
      <input type="password" name="password" use:validators={[required]} />
      <Hint for="password" on="required">This is a mandatory field</Hint>
    </div>
    
      <button on:click={handleLogin} disabled={!$form.valid}>Login</button>
    </form>
  </div>

</main>

<style>
  .loginform {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }

</style>
