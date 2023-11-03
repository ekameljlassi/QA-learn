<script>
    import { settings } from "../common/data/emailForm"
    import Select from 'svelte-select';
    import { DateInput } from 'date-picker-svelte'
  

    let hackerspaceCollection = [
        { value : 'tunisia', label: 'Tunisia Online Hackerspace' },
        { value : 'lagos', label: 'Lagos Hackerspace' },
        { value : 'abidjan', label: 'Abidjan Hackerspace' },
    ]

    let date = new Date()
</script>

<style>
    .container {
        width: 100%;
    }
    .title-container {
        font-size: 30px;
        color: black;
        display: flex;
        justify-content: center;
        padding: 20px 0;
    }

    .form-container {
        display: grid;
        grid-template-columns: 1fr auto;
    }
    .input-title {
        color: #828A92;
        font-size: 20px;
        padding: 10px 0;
        width: 300px;
    }
    .input-field-container {
        width: 300px;
    }
    .input-field {
        padding: 12px 15px;
        width: 300px;
        border-radius: 7px;
        background-color: white;
        border: 2px solid #EBECF0;
        color: #828A92;
    }
    .hs-select {
        width: 335px;
        color: #828A92;
    }
    .submit-button {
        background-color: #176FFF;
        width: 340px;
        height: 45px;
        margin-top: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
</style>


<div class="container">
    <div class="title-container">
        QA Learning Emails
    </div>
 <form class="form-container">
    {#each settings.input as field}
    {#if field.id != 'sessionDate' && field.id != 'Hackerspace'}
    <div class="input-container">
    <div class="input-title">
        {field.title}
    </div>
    <div class="input-field-container">
        <input class="input-field" type='text'
        placeholder={field.placeHolder}
        />
    </div>
</div>
    {/if}
    {#if field.id === "Hackerspace"}
    <div class="input-container">
    <div class="input-title">
    {field.title}
    </div>
    <div class="hs-select">
    <Select items={hackerspaceCollection} placeholder={field.placeHolder}
    --item-hover-bg="#176FFF"
    --border-focused="1px solid #176FFF"
    --item-is-active-bg="#176FFF">
    </Select>
    </div>
    </div>
    {/if}
    {#if field.id === "sessionDate"}
    <div class="input-container">
    <div class="input-title">
    {field.title}
    </div>
    <DateInput bind:value={date}/>
    </div>
    {/if}
    {/each}
    <button class="submit-button">
        Send Email
        <svg width="30" height="18" viewBox="0 0 33 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7.01067 5.67603H0V4.20935H7.01067V5.67603ZM7.01067 11.2934H1.40797V9.82668H7.01067V11.2934ZM7.01067 16.9107H2.80135V15.444H7.01067V16.9107ZM33 21.12H7.01064V19.6534H31.5333V1.46668H7.01067V0H33V21.12ZM19.6386 14.1078L6.49729 1.257L7.52398 0.20833L19.6387 12.0561L31.7533 0.20833L32.78 1.257L19.6386 14.1078ZM7.52988 20.9059L6.49291 19.869L16.3196 10.0423L17.3565 11.0793L7.52988 20.9059ZM31.7475 20.9059L21.9208 11.0792L22.9592 10.0409L32.7859 19.8675L31.7475 20.9059Z" fill="white"/>
            </svg>            
    </button>
</form>
</div>