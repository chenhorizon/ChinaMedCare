<template>
  <div class="hospital-card">
    <div class="card-image-wrapper">
      <img :src="hospital.image" :alt="hospital.name" class="card-image" />
      <div class="card-badges">
        <span v-if="hospital.accreditation" class="badge-accred">{{ hospital.accreditation }}</span>
      </div>
      <button class="card-favorite">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
        </svg>
      </button>
    </div>
    <div class="card-content">
      <div class="card-header">
        <div>
          <h3 class="card-title">{{ hospital.name }}</h3>
          <div class="card-location">
            <svg viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/>
            </svg>
            {{ hospital.location }}
          </div>
        </div>
        <div class="card-rating-wrapper">
          <div class="card-rating">
            <span class="rating-score">{{ hospital.rating }}</span>
            <span class="rating-label">Excellent</span>
          </div>
          <div class="rating-reviews">{{ hospital.reviews }} reviews</div>
        </div>
      </div>
      <div class="card-tags">
        <span v-for="dept in hospital.departments.slice(0, 3)" :key="dept" class="tag-dept">
          {{ dept }}
        </span>
      </div>
      <div class="card-languages">
        <svg viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6H10a3 3 0 013 3v.5a2.5 2.5 0 002.5 2.5h.5c.213 0 .417.034.61.097a6.002 6.002 0 01-8.778 6.175A4.996 4.996 0 017 15v-.5a2.5 2.5 0 00-2.5-2.5H4a.5.5 0 01-.5-.5v-.973c0-.358.072-.702.206-1.027a.5.5 0 01.626-.474z" clip-rule="evenodd"/>
        </svg>
        <span>{{ hospital.languages.join(', ') }}</span>
      </div>
      <div class="card-footer">
        <button class="btn-view">View Details</button>
        <button class="btn-book">Book Now</button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  hospital: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.hospital-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.hospital-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  height: 220px;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.hospital-card:hover .card-image {
  transform: scale(1.05);
}

.card-badges {
  position: absolute;
  top: 16px;
  left: 16px;
  display: flex;
  gap: 8px;
}

.badge-accred {
  background: #22c55e;
  color: white;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.card-favorite {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(8px);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #64748b;
}

.card-favorite:hover {
  background: white;
  color: #ef4444;
  transform: scale(1.05);
}

.card-favorite svg {
  width: 20px;
  height: 20px;
}

.card-content {
  padding: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 16px;
}

.card-title {
  font-size: 17px;
  font-weight: 800;
  color: #1e293b;
  margin: 0 0 6px;
  line-height: 1.3;
}

.card-location {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #64748b;
  font-size: 13px;
}

.card-location svg {
  width: 16px;
  height: 16px;
  color: #94a3b8;
}

.card-rating-wrapper {
  text-align: right;
  flex-shrink: 0;
}

.card-rating {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  background: #1e293b;
  color: white;
  padding: 8px 12px;
  border-radius: 10px;
  margin-bottom: 4px;
}

.rating-score {
  font-size: 18px;
  font-weight: 800;
  line-height: 1;
}

.rating-label {
  font-size: 11px;
  font-weight: 600;
  margin-top: 2px;
}

.rating-reviews {
  font-size: 12px;
  color: #64748b;
}

.card-tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 14px;
}

.tag-dept {
  padding: 4px 10px;
  background: #f1f5f9;
  color: #475569;
  font-size: 12px;
  font-weight: 500;
  border-radius: 6px;
}

.card-languages {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #64748b;
  font-size: 13px;
  margin-bottom: 18px;
  padding-bottom: 18px;
  border-bottom: 1px solid #f1f5f9;
}

.card-languages svg {
  width: 16px;
  height: 16px;
  color: #94a3b8;
  flex-shrink: 0;
}

.card-footer {
  display: flex;
  gap: 10px;
}

.btn-view {
  flex: 1;
  padding: 10px 16px;
  background: white;
  color: #1e293b;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-view:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.btn-book {
  flex: 1;
  padding: 10px 16px;
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-book:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
}
</style>
