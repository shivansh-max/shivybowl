import {RouterProvider} from "react-router-dom";
import Header from "./components/header/Header.jsx";
import router from "./public/router.jsx";


const App = () => {
	return <>
		<Header height={"150px"}/>
		<RouterProvider router={router}/>
	</>

};

export default App;