import { useState } from "react";
import API from "./api/blueprintApi";

function App() {
  const [requirement, setRequirement] = useState("");
  const [blueprint, setBlueprint] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateBlueprint = async () => {
    console.log("✅ Button Clicked");

    if (!requirement.trim()) {
      alert("Please enter your software idea.");
      return;
    }

    console.log("📤 Sending request to backend...");
    console.log("Requirement:", requirement);

    try {
      setLoading(true);
      const res = await API.post("/generate", {
        requirement: requirement,
      });

      // Save AI Response
      setBlueprint(res.data);
      setLoading(false);

      console.log("✅ Backend Response:");
      console.log(res.data);

      alert("Blueprint Generated Successfully 🚀");
    } catch (err) {
      console.error("❌ Error:");
      console.error(err);

      if (err.response) {
        console.log("Status:", err.response.status);
        console.log("Data:", err.response.data);
      }
      setLoading(false);
      alert("Generation Failed");
    }
  };

  // Download generated ZIP
  const downloadZip = () => {
    window.open("http://127.0.0.1:8000/download", "_blank");
  };

  return (
    <div className="relative min-h-screen overflow-hidden bg-[#F1F5F9] text-slate-800 antialiased selection:bg-sky-200 selection:text-sky-900">

      {/* Ambient Floating Soft Light Glows */}
      <div className="absolute top-12 left-1/4 h-[500px] w-[500px] rounded-full bg-sky-200/50 blur-[140px] pointer-events-none"></div>

      <div className="absolute bottom-10 right-1/4 h-[450px] w-[450px] rounded-full bg-indigo-200/40 blur-[150px] pointer-events-none"></div>

      <div className="relative z-10 mx-auto flex min-h-screen max-w-6xl flex-col items-center justify-center px-6 py-20">

        {/* Logo */}
        <h1 className="text-7xl md:text-8xl font-black tracking-tight bg-gradient-to-r from-slate-900 via-sky-900 to-slate-800 bg-clip-text text-transparent">
          Blueprint <span className="text-sky-600">AI</span>
        </h1>

        {/* Main Title */}
        <h2 className="mt-8 text-center text-5xl md:text-6xl font-extrabold text-slate-900 tracking-tight leading-tight">
          Build Software Architecture <br className="hidden md:inline" />
          <span className="bg-gradient-to-r from-sky-600 to-indigo-600 bg-clip-text text-transparent">
            From Your Idea
          </span>
        </h2>

        {/* Subtitle */}
        <p className="mt-6 max-w-2xl text-center text-lg leading-8 text-slate-600">
          Describe your application ideas in natural language. Get back full
          architecture schemas, API endpoints, folder structures, and starter
          code instantly.
        </p>

        {/* Input Card */}
        <div className="mt-12 w-full max-w-3xl rounded-[32px] border border-white/80 bg-white/60 p-6 shadow-[0_20px_50px_rgba(148,163,184,0.15)] backdrop-blur-xl">

          <textarea
            value={requirement}
            onChange={(e) => setRequirement(e.target.value)}
            className="h-60 w-full resize-none rounded-2xl border border-sky-100/80 bg-sky-50/40 p-6 text-base text-slate-800 placeholder:text-slate-400 outline-none backdrop-blur-sm transition-all duration-300 focus:border-sky-400 focus:bg-sky-50/80 focus:ring-4 focus:ring-sky-100"
            placeholder="Example: Build a Library Management System with Authentication, Book Management, Student Dashboard, REST APIs, JWT Authentication and PostgreSQL Database..."
          />

          
            <button
              onClick={generateBlueprint}
              disabled={loading}
              className={`mt-4 w-full rounded-2xl py-4 text-base font-semibold text-white shadow-lg backdrop-blur-md transition-all duration-300 ${
                loading
                  ? "bg-slate-400 cursor-not-allowed"
                  : "bg-gradient-to-r from-sky-500 to-indigo-600 hover:scale-[1.01] hover:shadow-sky-500/30 active:scale-[0.99]"
              }`}
                >
              {loading ? "⏳ Generating Blueprint..." : "⚡ Generate Blueprint"}
            </button>
          

        </div>

        {/* Feature Cards */}
        <div className="mt-14 grid w-full max-w-4xl gap-6 md:grid-cols-3">

          {/* AI Architecture */}
          <div className="group rounded-3xl border border-white/80 bg-white/50 p-7 shadow-[0_10px_30px_rgba(148,163,184,0.1)] backdrop-blur-lg transition-all duration-300 hover:-translate-y-1.5 hover:bg-white/80 hover:shadow-xl hover:shadow-sky-100">

            <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/80 bg-white/60 text-2xl shadow-sm backdrop-blur-md">
              🧠
            </div>

            <h3 className="mt-5 text-lg font-bold text-slate-900">
              AI Architecture
            </h3>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Generates clean, scalable software architecture specs directly from text.
            </p>

          </div>

          {/* Code & APIs */}
          <div className="group rounded-3xl border border-white/80 bg-white/50 p-7 shadow-[0_10px_30px_rgba(148,163,184,0.1)] backdrop-blur-lg transition-all duration-300 hover:-translate-y-1.5 hover:bg-white/80 hover:shadow-xl hover:shadow-sky-100">

            <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/80 bg-white/60 text-2xl shadow-sm backdrop-blur-md">
              ⚡
            </div>

            <h3 className="mt-5 text-lg font-bold text-slate-900">
              Code & APIs
            </h3>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Creates ready-to-run FastAPI, React, REST, database schemas, and folder setups.
            </p>

          </div>

          {/* Export Package */}
          <div className="group rounded-3xl border border-white/80 bg-white/50 p-7 shadow-[0_10px_30px_rgba(148,163,184,0.1)] backdrop-blur-lg transition-all duration-300 hover:-translate-y-1.5 hover:bg-white/80 hover:shadow-xl hover:shadow-sky-100">

            <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/80 bg-white/60 text-2xl shadow-sm backdrop-blur-md">
              📦
            </div>

            <h3 className="mt-5 text-lg font-bold text-slate-900">
              Export Package
            </h3>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Download your complete AI generated project as a ZIP file.
            </p>

            <button
              onClick={downloadZip}
              className="mt-5 w-full rounded-xl bg-gradient-to-r from-green-500 to-emerald-600 py-3 text-white font-semibold shadow-lg transition hover:scale-[1.02]"
            >
              📥 Download ZIP
            </button>

          </div>

        </div>
        {loading && (
  <div className="mt-12 w-full max-w-5xl rounded-3xl border border-sky-200 bg-white/70 p-8 shadow-xl backdrop-blur-xl">

    <div className="flex items-center gap-4">
      <div className="h-12 w-12 animate-spin rounded-full border-4 border-sky-500 border-t-transparent"></div>

      <div>
        <h2 className="text-3xl font-bold text-sky-700">
          🧠 AI is Building Your Blueprint
        </h2>

        <p className="mt-2 text-slate-600">
          Please wait while BlueprintAI designs your complete software architecture...
        </p>
      </div>
    </div>
    <div className="mt-8">
  <div className="h-3 w-full overflow-hidden rounded-full bg-slate-200">
    <div className="h-full w-full animate-pulse rounded-full bg-gradient-to-r from-sky-500 via-indigo-500 to-sky-500"></div>
  </div>

  <p className="mt-3 text-center text-sm text-slate-500">
    This may take a few minutes depending on the complexity of your project...
  </p>
</div>
    <div className="mt-8 space-y-4">

      <div className="flex items-center gap-3">
        <span className="text-green-600 text-xl">✅</span>
        <span>Understanding Requirements</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="animate-pulse text-blue-600 text-xl">⚙️</span>
        <span>Designing System Architecture</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="animate-pulse text-blue-600 text-xl">🗄️</span>
        <span>Generating Database Schema</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="animate-pulse text-blue-600 text-xl">🔌</span>
        <span>Creating REST APIs</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="animate-pulse text-blue-600 text-xl">📦</span>
        <span>Packaging Downloadable Project</span>
      </div>

    </div>

  </div>
)}
        {/* Generated Blueprint */}

        {blueprint && (
          <div className="mt-16 w-full max-w-5xl rounded-3xl border border-sky-200 bg-white/70 p-8 shadow-xl backdrop-blur-xl">

            <h2 className="mb-6 text-3xl font-bold text-sky-700">
              🚀 Generated Blueprint
            </h2>

            <pre className="overflow-auto whitespace-pre-wrap rounded-2xl bg-slate-50 p-6 text-sm text-slate-700">
              {JSON.stringify(blueprint, null, 2)}
            </pre>
          <div className="mt-8 flex justify-center">
  <a
    href="http://127.0.0.1:8000/download"
    target="_blank"
    rel="noopener noreferrer"
    className="rounded-2xl bg-gradient-to-r from-green-500 to-emerald-600 px-8 py-4 text-lg font-bold text-white shadow-lg transition hover:scale-105"
  >
    📦 Download Generated Project (.zip)
  </a>
</div>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;