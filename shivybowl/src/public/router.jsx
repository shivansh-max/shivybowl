import {createBrowserRouter} from "react-router-dom";
import Sets from "../pages/Sets.jsx";
import Home from "../pages/Home.jsx";

const router = createBrowserRouter([
	{
		path: "/",
		element: <Home />,
		errorElement: <Home />
	},
	{
		path: "/sets",
		element: <Sets/>
	},
]);

export default router;