var $E = function(selector, filter) {return ($(filter) || document).getElement(selector);};
var $ES = function(selector, filter) {return ($(filter) || document).getElements(selector);};

var paad = {
	events: new Composer.Event(),

	// our salty core communication lib(eral tears).
	core: null,

	// our "remember paad" lib. REMEMBERRR
	remember_me: null,

	// holds the DOM object that paad does all of its operations within
	main_container_selector: '#main',

	// global key handler for attaching keyboard events to the app
	keyboard: null,

	// a modal helper
	overlay: null,

	initialized: false,
	loaded: false,

	// holds the title breadcrumbs
	titles: [],

	controllers: {
		pages: null,
		header: null,
		nav: null,
		sidebar: null,
		loading: null
	},
