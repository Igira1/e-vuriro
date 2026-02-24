import React from 'react';
import { Link } from 'react-router-dom';

const Landing: React.FC = () => {
  return (
    <div className="min-h-screen bg-blue-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="text-2xl font-bold text-blue-600">TeleMed</div>
            <nav className="space-x-4">
              <Link to="/login" className="text-blue-600 hover:text-blue-800">Login</Link>
              <Link to="/register" className="bg-blue-600 text-white px-4 py-2 rounded">Get Started</Link>
            </nav>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Remote Healthcare, Anytime, Anywhere</h1>
          <p className="text-xl text-gray-600 mb-8">Connect with doctors through video consultations, manage your health records, and get AI-powered insights.</p>
          <Link to="/register" className="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg">Book Appointment</Link>
        </div>
      </main>
    </div>
  );
};

export default Landing;