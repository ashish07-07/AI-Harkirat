
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [hover, setHover] = useState(false);
  const router = useRouter();

  return (
    <div
      style={{
        height: "100vh",
        backgroundColor: "black",
        color: "white",
        fontFamily: "cursive",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {/* Title */}
      <div style={{ padding: "40px 0", textAlign: "center" }}>
        <h1
          style={{
            fontSize: "64px",
            fontWeight: "bold",
            letterSpacing: "2px",
            textShadow: "2px 2px 4px rgba(255,255,255,0.2)",
          }}
        >
          Animation Generation
        </h1>
      </div>

      {/* Center Section */}
      <div
        style={{
          flex: 1,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: "20px",
          fontSize: "22px",
        }}
      >
        <h2 style={{ fontWeight: "bold" }}>
          Just Describe It. We'll Animate It.
        </h2>
        <p style={{ maxWidth: "600px", textAlign: "center", opacity: 0.9 }}>
          Generate your own AI-powered animation by simply typing out your scene
          in 3 short lines. Now with voice too!
        </p>

        {/* Button */}
        <button
          onClick={() => router.push("/userscene")}
          onMouseEnter={() => setHover(true)}
          onMouseLeave={() => setHover(false)}
          style={{
            marginTop: "10px",
            padding: "12px 28px",
            border: `2px solid ${hover ? "skyblue" : "white"}`,
            borderRadius: "30px",
            background: "transparent",
            color: "white",
            fontSize: "20px",
            cursor: "pointer",
            transition: "all 0.3s ease",
            transform: hover ? "scale(1.05)" : "scale(1)",
            boxShadow: hover ? "0 0 10px skyblue" : "none",
          }}
        >
         Check It out Here
        </button>
      </div>
    </div>
  );
}

