require 'spec_helper'

describe server(:app) do
	describe http('http://example.com')do
		it "content includes Example Domain" do
			expect(response.body).to include('Example Domain')
		end
		it "tesponds as text/html" do
			expect(response.headers['content-type']).to eq("text/html")
		end
		it "has an ETage reader" do
			expect(response.headers).to include('ETag')
		end
	end
end
